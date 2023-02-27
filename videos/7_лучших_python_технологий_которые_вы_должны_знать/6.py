
import readline
import rlcompleter


"""
Запускаем встроенное автодополнение при нажатии tab.
Работает в оболочках, которые не содержат подсказок.
"""

key = "space"
readline.parse_and_bind(f"{key}: complete")