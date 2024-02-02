def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        if 'result' not in locals():
            print("Finally: Division result is not available.")
        else:
            print("Finally: Division completed successfully.")
