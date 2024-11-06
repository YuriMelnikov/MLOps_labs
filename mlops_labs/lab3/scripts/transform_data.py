import pandas as pd


def transform_data(input_path, output_path):
    try:
        # Загружаем данные
        data = pd.read_csv(input_path)

        # Шаг 1: Удаление ненужных столбцов
        columns_to_drop = [
            "Name",
            "Ticket",
            "Cabin",
        ]  # Удаляем столбцы, которые могут быть неважны для анализа
        data = data.drop(columns=columns_to_drop, errors="ignore")

        # Шаг 2: Обработка пропущенных значений
        # Заполним возраст медианой, а остальные пропуски удалим
        if "Age" in data.columns:
            data["Age"] = data["Age"].fillna(
                data["Age"].median()
            )  # Измените эту строку
        data.dropna(inplace=True)

        # Шаг 3: Создание нового признака 'AgeGroup' - группа возрастов
        if "Age" in data.columns:
            bins = [0, 12, 18, 35, 60, 100]
            labels = ["Child", "Teenager", "Adult", "Mid-Age", "Senior"]
            data["AgeGroup"] = pd.cut(data["Age"], bins=bins, labels=labels)

        # Шаг 4: Кодирование категориальных переменных
        data = pd.get_dummies(
            data, columns=["Sex", "Embarked", "AgeGroup"], drop_first=True
        )

        # Сохраняем преобразованные данные
        data.to_csv(output_path, index=False)
        print(f"Data transformed and saved to {output_path}")
    except Exception as e:
        print(f"Failed to transform data: {e}")


if __name__ == "__main__":
    input_path = "./mlops_labs/lab3/data/titanic.csv"
    output_path = "./mlops_labs/lab3/data/transformed_titanic.csv"
    transform_data(input_path, output_path)
