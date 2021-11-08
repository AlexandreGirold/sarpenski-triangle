def sarpenski_carpet(n):
    end=""
    etoile="*"
    espace=" "
    if n == 0:
        "n doit etre plus grand que 0"
    pascal = [[1]]

    for i in range(1, n):
        line = [1]
        for j in range(len(pascal)):
            if j + 1 < len(pascal):
                line.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
        line.append(1)
        pascal.append(line)
    for l in pascal:
        for e in l:
            if e % 2 == 0 :
                end+=espace
            else:
                end+=etoile
        end+="\n"

    return end
