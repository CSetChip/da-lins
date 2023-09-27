def conta_vogais(texto:str) -> int:
    return len(list(filter(lambda char: char.lower() in 'aeiou', texto)))

print('Total De vogais:', conta_vogais("casa"))