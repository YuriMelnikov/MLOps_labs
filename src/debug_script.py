def greet(name: str) -> str:
    greeting = f"Hello, {name}!"
    return greeting


if __name__ == "__main__":
    print(greet("MlOps_labs"))
    #   print(greet(123))  # Ошибка типов для проверки mypy

# Появляется ошибка при коммите:
# src\debug_script.py:7: error: Argument 1 to "greet" has incompatible type "int"; expected "str"
# Found 1 error in 1 file (checked 1 source file)
