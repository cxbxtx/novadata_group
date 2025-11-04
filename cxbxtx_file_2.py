def analyze_text_file(filename):
    """
    Анализирует текстовый файл и выводит статистику:
    - количество строк
    - количество слов
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            
            # Базовая статистика
            line_count = len([line for line in lines if line.strip()])
            word_count = len(content.split())
            char_count = len(content)
            
            # Анализ частоты слов
            words = content.lower().split()
            word_freq = {}
            
            for word in words:
                # Убираем знаки препинания
                clean_word = ''.join(char for char in word if char.isalnum())
                if clean_word:
                    word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
            
            
            # Выводим результаты
            print(f"Анализ файла: {filename}")
            print(f"Количество строк: {line_count}")
            print(f"Количество слов: {word_count}")
            
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Использование функции
if __name__ == "__main__":
    # Создаем тестовый файл для демонстрации
    sample_text = """Привет, мир!
Это тестовый файл для демонстрации работы программы.
Программа анализирует текст и выводит статистику.
Привет еще раз!"""
    
    with open('test_file.txt', 'w', encoding='utf-8') as f:
        f.write(sample_text)
    
    # Анализируем созданный файл
    analyze_text_file('test_file.txt')