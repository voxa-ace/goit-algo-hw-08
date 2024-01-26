# Оптимізатор З'єднання Мережевих Кабелів

## Огляд
Цей Python скрипт надає рішення для ефективного з'єднання декількох мережевих кабелів з метою мінімізації загальних витрат на з'єднання. Він використовує алгоритм мінімальної купи (min heap), щоб забезпечити якомога більш економічний процес з'єднання.

## Особливості
- **Алгоритм Мінімальної Купи**: Використовує мінімальну купу для ефективного з'єднання кабелів.
- **Мінімізація Витрат**: Завжди з'єднує два найкоротші кабелі, щоб мінімізувати загальні витрати.
- **Обробка Порожнього Списку**: Коректно обробляє випадки з порожнім списком кабелів, повертаючи витрати рівні 0.

## Функціональність
Скрипт приймає список довжин мережевих кабелів та використовує алгоритм мінімальної купи для їх з'єднання. Завдання полягає у з'єднанні кабелів попарно, починаючи з двох найкоротших, для досягнення мінімальної суми витрат на з'єднання.
