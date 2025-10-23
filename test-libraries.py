import os
import sys
from pathlib import Path

#создание папки результатов
RESULTS_DIR = Path("./test_results")
RESULTS_DIR.mkdir(exist_ok=True)

def test_numpy():
    """Тест NumPy"""
    try:
        import numpy as np  #импорт
        print("NumPy импортирован")
        
        #создание массива, проверка
        x = np.linspace(0, 2*np.pi, 1000)
        print(f"Массив создан: {len(x)} элементов")
        
        #точность cos, проверка
        cos_true = np.cos(x)
        error = np.max(np.abs(cos_true - np.cos(x)))
        print(f"Точность cos: {error:.2e}")
        
        #сохранение данных
        np.savetxt(RESULTS_DIR / "test_numpy_data.txt", 
                  np.column_stack([x, cos_true]))
        return True
    except ImportError:
        print("NumPy НЕ УСТАНОВЛЕН! pip install numpy")
        return False
    except Exception as e:
        print(f"NumPy ошибка: {e}")
        return False

def test_matplotlib():
    """Тест Matplotlib"""
    try:
        import matplotlib.pyplot as plt  # ИМПОРТ ЗДЕСЬ!
        import numpy as np  # Импорт для данных
        print("Matplotlib импортирован")
        
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(x)
        
        plt.figure(figsize=(8, 4))
        plt.plot(x, y, 'b-', linewidth=2)
        plt.title('Тестовый график')
        plt.xlabel('x')
        plt.ylabel('sin(x)')
        plt.grid(True, alpha=0.3)
        plt.savefig(RESULTS_DIR / 'test_plot.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("График сохранён!")
        return True
    except ImportError:
        print("Matplotlib НЕ УСТАНОВЛЕН! pip install matplotlib")
        return False
    except Exception as e:
        print(f"Matplotlib ошибка: {e}")
        return False

def test_animation():
    """Тест анимации"""
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        from matplotlib.animation import FuncAnimation  #импорт
        print("Animation импортирован")
        
        fig, ax = plt.subplots()
        x = np.linspace(0, 2*np.pi, 100)
        line, = ax.plot(x, np.sin(x))
        
        def animate(frame):
            line.set_ydata(np.sin(x + frame/10))
            return line,
        
        
        anim = FuncAnimation(fig, animate, frames=10, interval=100, blit=True)
        anim.save(RESULTS_DIR / 'test_animation.gif', writer='pillow', fps=10)
        plt.close()
        print("Анимация сохранена!")
        return True
    except ImportError:
        print("Animation НЕ УСТАНОВЛЕН! pip install matplotlib")
        return False
    except Exception as e:
        print(f"Animation ошибка: {e}")
        return False

if __name__ == "__main__":
    print("=== ТЕСТИРОВАНИЕ БИБЛИОТЕК ===")
    tests = [
        ("NumPy", test_numpy),
        ("Matplotlib", test_matplotlib),
        ("Animation", test_animation)
    ]
    
    all_passed = True
    for name, test_func in tests:
        result = test_func()
        if result:
            print(f"✓ {name}: PASS\n")
        else:
            print(f"✗ {name}: FAIL\n")
            all_passed = False
    
    if all_passed:
        print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ! МОЖНО ИДТИ ДАЛЬШЕ!")
        sys.exit(0)
    else:
        print("УСТАНОВИ БИБЛИОТЕКИ:")
        print("pip install numpy matplotlib")
        sys.exit(1)