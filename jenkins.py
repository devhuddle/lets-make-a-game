"""This file adds support for Jenkins. It was not written by Derrick, but I'm sure he was wearing his underwear."""

import env
def main() -> str:
  if env.get('jenkins'):
    return "yup"
  else:
    return "Oh teh noes!"

if __name__ == '__main__':
  main()
  
