echo "Docker Cleaner Script"
echo "1) Полностью удалить всё (контейнеры, образы, тома, сети — включая базу данных)"
echo "2) Удалить всё, кроме контейнера с базой данных (postgres)"
read -p "Выберите режим (1 или 2): " mode

if [[ "$mode" == "1" ]]; then
    echo "Остановка всех контейнеров..."
    docker stop $(docker ps -aq) 2>/dev/null

    echo "Удаление всех контейнеров..."
    docker rm -f $(docker ps -aq) 2>/dev/null

    echo "Удаление всех образов..."
    docker rmi -f $(docker images -q) 2>/dev/null

    echo "Удаление всех томов..."
    docker volume rm $(docker volume ls -q) 2>/dev/null

    echo "Удаление всех пользовательских сетей..."
    docker network rm $(docker network ls -q | grep -vE 'bridge|host|none') 2>/dev/null

    echo "Глубокая очистка мусора..."
    docker system prune -a --volumes -f

    echo "Все объекты Docker удалены."

elif [[ "$mode" == "2" ]]; then
    echo "Остановка всех контейнеров, кроме postgres..."
    docker ps -q --filter "name=postgres" | xargs -r echo "Пропущен контейнер:"

    for id in $(docker ps -aq); do
        name=$(docker inspect --format='{{.Name}}' $id | sed 's/^\/\+//')
        if [[ "$name" != *postgres* ]]; then
            echo "Остановка контейнера: $name"
            docker stop $id 2>/dev/null
            docker rm -f $id 2>/dev/null
        else
            echo "Пропущен контейнер БД: $name"
        fi
    done

    echo "Удаление неиспользуемых образов..."
    docker image prune -a -f

    echo "Удаление неиспользуемых томов (БД останется)..."
    docker volume prune -f

    echo "Удаление неиспользуемых сетей..."
    docker network prune -f

    echo "Очистка завершена. База данных сохранена."

else
    echo "Некорректный выбор режима. Завершение работы."
    exit 1
fi