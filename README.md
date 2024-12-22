# Robot Vacuum Pathfinding

## Description
This project simulates a robot vacuum with features like manual control, autonomous navigation, lidar visualization, and dynamic grid updates. The robot can navigate through a customizable grid while avoiding obstacles and plotting an optimal path to a specified target.

## Features
- **Manual Control**: Use `W`, `A`, `S`, `D` keys to move the robot in small steps (0.1 grid unit).
- **Autonomous Navigation**: Press `P` to enable pathfinding to the target point using the A* algorithm.
- **Obstacle Management**: Add/remove obstacles on the grid with mouse clicks.
- **Lidar Simulation**: Visualize the lidar scanning in real-time.
- **Path Visualization**: View the path traveled by the robot.
- **Speed Adjustment**: Use arrow keys to adjust the robot's speed.
- **Reset Functionality**: Reset the grid and robot state with `R`.

## Dependencies
This project requires the following Python libraries:
- `pygame`
- `numpy`

You can install the dependencies using pip:
```bash
pip install pygame numpy
```

## Controls
- **W/A/S/D**: Move the robot in the respective direction.
- **R**: Reset the simulation.
- **P**: Enable autonomous mode.
- **Mouse Left Click**: Add an obstacle at the clicked location.
- **Mouse Right Click**: Remove an obstacle at the clicked location.
- **Arrow Up**: Decrease robot speed.
- **Arrow Down**: Increase robot speed.

## How to Run
1. Install the required dependencies.
2. Run the script using Python:
   ```bash
   python robot_vacuum.py
   ```
3. Interact with the simulation using the controls above.

## File Download
You can download the script file directly from the link below:
[Download robot_vacuum.py](sandbox:/mnt/data/robot_vacuum.py)

## Additional Notes
- Ensure your Python version is 3.6 or higher.
- Use a screen resolution that supports a 600x400 window for the best experience.

Enjoy navigating your robot vacuum!

# Робот-пылесос: Поиск пути

## Описание
Этот проект симулирует робота-пылесоса с функциями ручного управления, автономной навигации, визуализации данных лидара и динамического обновления сетки. Робот может перемещаться по настраиваемой сетке, избегая препятствий и прокладывая оптимальный маршрут к указанной цели.

## Функции
- **Ручное управление**: Используйте клавиши `W`, `A`, `S`, `D` для перемещения робота небольшими шагами (0.1 сетки).
- **Автономная навигация**: Нажмите `P` для включения режима поиска пути к целевой точке с использованием алгоритма A*.
- **Управление препятствиями**: Добавляйте/удаляйте препятствия на сетке с помощью кликов мыши.
- **Симуляция лидара**: Визуализируйте сканирование лидара в реальном времени.
- **Визуализация пути**: Просматривайте пройденный роботом маршрут.
- **Настройка скорости**: Используйте стрелки для изменения скорости робота.
- **Сброс состояния**: Сбрасывайте сетку и состояние робота клавишей `R`.

## Зависимости
Проект требует установки следующих библиотек Python:
- `pygame`
- `numpy`

Установите зависимости с помощью pip:
```bash
pip install pygame numpy
```

## Управление
- **W/A/S/D**: Перемещение робота в соответствующем направлении.
- **R**: Сброс симуляции.
- **P**: Включение автономного режима.
- **Левая кнопка мыши**: Добавление препятствия в указанной точке.
- **Правая кнопка мыши**: Удаление препятствия в указанной точке.
- **Стрелка вверх**: Уменьшение скорости робота.
- **Стрелка вниз**: Увеличение скорости робота.

## Как запустить
1. Установите необходимые зависимости.
2. Запустите скрипт с помощью Python:
   ```bash
   python robot_vacuum.py
   ```
3. Взаимодействуйте с симуляцией, используя указанные элементы управления.

## Ссылка для скачивания
Вы можете скачать файл скрипта по ссылке ниже:
[Download robot_vacuum.py](sandbox:/mnt/data/robot_vacuum.py)

## Дополнительные примечания
- Убедитесь, что версия Python 3.6 или выше.
- Для лучшего опыта используйте разрешение экрана, поддерживающее окно 600x400.

Приятного использования!
