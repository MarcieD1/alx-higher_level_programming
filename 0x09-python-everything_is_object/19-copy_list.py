#!/usr/bin/python3

def copy_list(l):
  """Return a copy of the list."""
  return l[:]

def main():
  """Copy a list."""
  l = [1, 2, 3]
  copy_l = copy_list(l)
  print(copy_l)

if __name__ == "__main__":
  main()
