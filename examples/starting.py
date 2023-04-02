from jsonxx import load_advanced

a = load_advanced("1.json", 4, "{}")
a[1] = 2
