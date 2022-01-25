import sys

ids = {}
functions = {}
function_arguments = {}
didBreak = False
didContinue = False
didReturn = False
locals = [[]]
functions = {}
function_arguments = {}
foundError = False
returnValue = None


def executeIfBlock(insts):
    global ids, didBreak, didContinue, locals, didReturn, foundError, returnValue
    locals.append([])
    for i in insts:
        if didBreak == True:  # case where a block inside this block triggered break, we shouldnt keep executing the current if block
            break
        elif i == 'bahar':
            # dans les instruction de if, si on trouve "bahar" c'est qu'on doit sortir du while,
            # donc j'ai defini cette variable global, qu'on va verifier dans while pour voir si on a break ou non,
            # si elle appartient au instructions qui se trouve dans if, je donne true a la variable global,
            #  et je ne termine pas les autre, instruction
            didBreak = True
            break
        elif didContinue == True:
            break
        elif i == 'chalu':
            # meme principe que break
            didContinue = True
            break
        elif didReturn:
            break
        elif i[0] == 'moklo':
            didReturn = True
            returnValue = run(i)
            break
        run(i)
    for i in locals[len(locals)-1]:
        ids.pop(i)
    locals.pop()


def executeWhileLoop(p):
    global ids, didBreak, didContinue, locals, didReturn, foundError, returnValue
    # on donne a ces variables false au cas ou elle sont devenu true suite a autre boucle
    didBreak = False
    didContinue = False
    locals.append([])
    while run(p[1]):
        for i in p[2]:
            # si parmis les instructions qui se trouve directement dans le block de while, je sort de la boucle for,
            # et du coups en entre pas dans else donc on sort de while(see for/else dans python)
            if i == 'bahar':
                break
            elif i == 'chalu':
                didContinue = True
                break
            elif didBreak == True:
                # je verifie sinon si un if qui s'est executé dans ce block contient un break('bahar'),
                #  si oui il aura changé didBreak en TRUE, et du coups on va sortir de ce while,
                didBreak = False
                break
            elif didContinue == True:
                break
            elif didReturn:
                break
            elif i[0] == 'moklo':
                didReturn = True
                returnValue = run(i)
                break
            else:
                run(i)
        else:
            continue
        if(didContinue == True):  # in the case of continue, we dont want to exit the loop
            didContinue = False
            continue
        break
    for i in locals[len(locals)-1]:
        ids.pop(i)
    locals.pop()


def executeDoWhileLoop(p):
    global ids, didBreak, didContinue, locals, didReturn, foundError, returnValue
    didBreak = False
    didContinue = False
    locals.append([])
    while(True):
        for i in p[1]:
            if i == 'bahar':
                break
            if i == 'chalu':
                didContinue = True
                break
            elif didBreak == True:
                didBreak = False
                break
            elif didContinue == True:
                break
            elif didReturn:
                break
            elif i[0] == 'moklo':
                didReturn = True
                returnValue = run(i)
                break
            else:
                run(i)
        else:
            if(run(p[2])):
                continue
        if(didContinue == True):  # in the case of continue, we dont anent to exit the loop
            didContinue = False
            if(run(p[2])):
                continue
        break
    for i in locals[len(locals)-1]:
        ids.pop(i)
    locals.pop()


def executeForLoop(p):
    global ids, didBreak, didContinue, locals, didReturn, foundError, returnValue
    didBreak = False
    didContinue = False
    locals.append([])
    if p[1][0] == '=':
        run(p[1])
    while run(p[2]):
        for i in p[4]:
            if i == 'bahar':
                break
            elif i == "chalu":
                didContinue = True
                break
            elif didBreak == True:
                didBreak = False
                break
            elif didContinue == True:
                break
            elif didReturn:
                break
            elif i[0] == 'moklo':
                didReturn = True
                returnValue = run(i)
                break
            else:
                run(i)
        else:
            run(p[3])
            continue
        if(didContinue == True):  # in the case of continue, we dont want to exit the loop
            didContinue = False
            run(p[3])
            continue
        break
    for i in locals[len(locals)-1]:
        ids.pop(i)
    locals.pop()


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def exitDarija():
    if len(sys.argv) > 1:
        exit()


def run(p):
    global ids, didBreak, didContinue, locals, didReturn, foundError, returnValue
    if type(p) == tuple:
        if(p[0] == 'prog'):
            for i in p[1]:
                run(i)
        try:
            if p[0] == '+':
                try:
                    return run(p[1]) + run(p[2])
                except TypeError:
                    # number and string concatenation
                    return str(run(p[1])) + str(run(p[2]))
            elif p[0] == '-':
                return run(p[1]) - run(p[2])
            elif p[0] == '*':
                return run(p[1]) * run(p[2])
            elif p[0] == '/':
                return run(p[1]) / run(p[2])
            elif p[0] == '%':
                return run(p[1]) % run(p[2])
            elif p[0] == '^':
                return run(p[1]) ** run(p[2])
            elif p[0] == '++':
                ids[p[1]] = ids[p[1]] + 1
                return ids[p[1]]
            elif p[0] == '--':
                ids[p[1]] = ids[p[1]] - 1
                return ids[p[1]]
            elif p[0] == 'neg':
                return -run(p[1])
        except TypeError:
            print("Had l'operation li 7awetli kro maymknch!")
            exitDarija()
        if p[0] == '=':
            if p[1][0] == 'arrelt':
                # dimension are stored in a table(p[1][2]), so the objective is to arrive at ids[p[1][1]][1stDim][2ndDim]...[lastDim],
                #  and since wheb having array = array, they will share the same memory allocation and any change that happens to one
                #  will happen to the other, with a loop, we advance until we arrive at the dimension before last then
                # we modify the value, we stop at the before last so that our variable would still be a table and would still share
                #  the same memory as our table in "ids"
                tab = ids[p[1][1]]
                j = len(p[1][2])-1
                t = 0
                for i in p[1][2]:
                    if t < j:
                        tab = tab[run(i)]
                    else:
                        break
                    t = t+1
                tab[p[1][2][run(j)]] = run(p[2])
            else:
                if p[1] == 'mojod':
                    ids[p[2][1]] = run(p[2][2])
                    locals[0].append(p[1])
                else:
                    var = run(p[2])
                    if type(var) is list:
                        # this is so we can assigne array to another without the seconde changing if the first does, since they wont be binded
                        ids[p[1]] = var[:]
                    else:
                        ids[p[1]] = var
                    exists = False
                    for i in locals:
                        if p[1] in i:
                            exists = True
                            break
                    if not(exists):
                        locals[len(locals)-1].append(p[1])
        elif p[0] == 'id':
            try:
                return ids[p[1]]
            except KeyError:
                print("lvariable '"+p[1]+"' makaynach")
                exitDarija()
        elif p[0] == 'chhapo':
            if len(p) == 2:
                toWrite = run(p[1])
                if type(toWrite) == bool:
                    if toWrite:
                        print("sachu")
                    else:
                        print("khotu")
                else:
                    print(toWrite)
            else:
                print(run(p[1]), run(p[2]))
        elif p[0] == 'arrelt':
            try:
                tab = ids[p[1]]
                for i in p[2]:
                    tab = tab[run(i)]
                return tab
            except TypeError:
                print("l'indice li 3titi fih mochkil")
                exitDarija()
            except KeyError:
                print("lvariable '"+p[1]+"' makaynach")
                exitDarija()
        elif p[0] == 'slice':
            try:
                if len(p) == 5:
                    return ids[p[1]][run(p[2]):run(p[4])]
                elif len(p) == 2:
                    return ids[p[1]][:]
                elif len(p) == 4:
                    return ids[p[1]][:run(p[3])]
                else:
                    return ids[p[1]][run(p[2]):]
            except TypeError:
                print('T9d t9sm ghir lists athva joumal!')
                exitDarija()
        elif p[0] == 'arrfn':
            try:
                if p[2] == 'jodo':
                    ids[p[1]].append(run(p[3]))
                elif p[2] == 'kber':
                    ids[p[1]].extend(run(p[3]))
                elif p[2] == 'khwi':
                    ids[p[1]].clear()
                elif p[2] == 'dkhel':
                    ids[p[1]].insert(run(p[3]), run(p[4]))
                elif p[2] == 'hatavo':
                    if len(p) == 3:
                        ids[p[1]].pop()
                    else:
                        ids[p[1]].pop(run(p[3]))
            except TypeError:
                print("'"+p[2]+"' Kat khdm ghir m3a tableau")
                exitDarija()
        elif p[0] == 'ane':
            return run(p[1]) and run(p[2])
        elif p[0] == 'ya':
            return run(p[1]) or run(p[2])
        elif p[0] == 'comp':
            try:
                if p[1] == '==':
                    return run(p[2]) == run(p[3])
                elif p[1] == '!=':
                    return run(p[2]) != run(p[3])
                elif p[1] == '>=':
                    return run(p[2]) >= run(p[3])
                elif p[1] == '<=':
                    return run(p[2]) <= run(p[3])
                elif p[1] == '>':
                    return run(p[2]) > run(p[3])
                elif p[1] == '<':
                    return run(p[2]) < run(p[3])
            except TypeError:
                print("Maymknch kro had lmo9arana '" +
                      p[1]+"' bles types li 3titi")
                exitDarija()

        elif p[0] == 'nahi':
            return not(run(p[1]))
        elif p[0] == 'kul':
            try:
                return len(run(p[1]))
            except TypeError:
                print("Kat khdm ghir m3a list athva jomla")
        elif p[0] == "jo":
            if run(p[1]):
                executeIfBlock(p[2])
            else:
                if len(p) > 3:
                    executeIfBlock(p[3])

        elif p[0] == "jya":
            executeWhileLoop(p)

        elif p[0] == "mate":
            executeForLoop(p)
        elif p[0] == 'kro':
            executeDoWhileLoop(p)
        elif p[0] == 'mahiti':
            if p[1] == ')':
                inp = input()
            else:
                inp = input(run(p[1])+'\n')
            if is_number(inp):
                inp = float(inp)
                if inp % int(inp) == 0:
                    return(int(inp))
                else:
                    return(inp)
            else:
                return(inp)

        elif p[0] == "prayas":
            if len(p) == 4:
                try:
                    for i in p[1]:
                        run(i)
                except:
                    for i in p[3]:
                        run(i)
            else:
                try:
                    for i in p[1]:
                        run(i)
                except:
                    for i in p[3]:
                        run(i)
                finally:
                    for i in p[5]:
                        run(i)
        elif p[0] == 'moklo':
            return(run(p[1]))
        elif p[0] == "banavo":
            if p[1] in functions:
                print("had lfonction '", p[1], "' déja kayna")
                exitDarija()
            if(len(p) == 4):
                function_arguments[p[1]] = p[2]
                for i in p[2]:
                    ids[i] = 0
                functions[p[1]] = p[3]
            else:
                functions[p[1]] = p[2]
        elif p[0] == "appel_func":
            if p[1] not in functions:
                print("Lfonction '", p[1], "' makaynach")
                exitDarija()
            if (p[1] in function_arguments and len(p) == 2):
                print("Lfonction '",
                      p[1], "' khassha des arguments")
                exitDarija()
            elif len(p) == 3:
                k = 0
                if(len(p[2]) != len(function_arguments[p[1]])):
                    print(
                        "l3adad dles arguments dyal la fonction '", p[1], "' machi howa hadak")
                    exitDarija()
                for i in function_arguments[p[1]]:
                    ids[i] = run(p[2][k])
                    k = k+1
            locals.append([])
            didReturn = False
            returnValue = None
            for i in functions[p[1]]:
                if i[0] == "moklo":
                    toReturn = run(i[1])  # before deleting local variable
                    for j in locals[len(locals)-1]:
                        ids.pop(j)
                    locals.pop()
                    return toReturn
                run(i)
                if didReturn:  # this should be after run, because if 'moklo' is the last instruction, we wont re-entre the loop to check for didReturn
                    for j in locals[len(locals)-1]:
                        ids.pop(j)
                    locals.pop()
                    didReturn = False  # if this isn't here, if we call function inside a loop, we will get out of the loop, it will case a break from loop
                    return returnValue
                    break
            for j in locals[len(locals)-1]:
                ids.pop(j)
            locals.pop()

    else:
        return p
