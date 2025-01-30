import argparse
import re

def remove_http_prefix(url):
    return re.sub(r'^https?://', '', url)

def process_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                print(remove_http_prefix(line.strip()))
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_path}' não encontrado.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove http:// e https:// do início de URLs.")
    parser.add_argument("-l", "--lista", help="Arquivo contendo a lista de URLs", required=True)
    args = parser.parse_args()
    process_list(args.lista)
