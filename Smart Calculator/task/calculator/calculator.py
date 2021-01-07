
if __name__ == '__main__':
    variables = {}
    while True:
        string_expression = input()
        string_expression = string_expression.replace(' ', '')

        if string_expression == '':
            continue

        if '/help' in string_expression:
            print('The program calculates the sum of numbers')
            continue

        if '/exit' in string_expression:
            print('Bye!')
            break

        if string_expression.startswith('/'):
            print('Unknown command')
            continue

        if string_expression.find('=') >= 0:
            try:
                name, value = string_expression.split('=')
                has_digit = False
                for char in name:
                    if char.isdigit():
                        has_digit = True
                        break
                if has_digit:
                    print('Invalid identifier')
                    continue

                if value[0].isalpha():
                    if value not in variables.keys():
                        print('Unknown variable')
                        continue
                    variables[name] = variables[value]
                else:
                    has_not_digit = False
                    for char in value:
                        if not(char.isdigit() or char in '+-'):
                            has_not_digit = True
                            break
                    if has_not_digit:
                        print('Invalid assignment')
                        continue
                    variables[name] = value
                continue
            except ValueError:
                print('Invalid assignment')
                continue

        if string_expression.endswith(('+', '-')):
            print('Invalid expression')
            continue

        while True:
            make_changes = False
            while True:
                pos = string_expression.find('++')
                if pos < 0:
                    break
                string_expression = string_expression.replace('++', '+')
                make_changes |= True

            while True:
                pos = string_expression.find('--')
                if pos < 0:
                    break
                string_expression = string_expression.replace('--', '+')
                make_changes |= True

            while True:
                pos = string_expression.find('+-')
                if pos < 0:
                    break
                string_expression = string_expression.replace('+-', '-')
                make_changes |= True

            while True:
                pos = string_expression.find('-+')
                if pos < 0:
                    break
                string_expression = string_expression.replace('-+', '-')
                make_changes |= True

            if not make_changes:
                break

        string_expression = string_expression.replace('+', ' +').replace('-', ' -')
        # print(str)

        decode_list = []
        calc_list = string_expression.split()
        has_error = False
        for item in calc_list:
            first = 0
            if item.startswith(('+', '-')):
                first = 1
            if item[first].isalpha():
                var_key = item[first:]
                if var_key not in variables.keys():
                    print('Unknown variable')
                    has_error = True
                    break
                decode_list.append(item[:first] + variables[var_key])
                continue
            decode_list.append(item)
        if has_error:
            continue

        print(sum(int(i) for i in decode_list))
