# Complete the solve function below.
# https://www.programiz.com/python-programming/methods/string/capitalize
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()