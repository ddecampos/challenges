class JustifyText():
    
    def __init__(self, text, length):
        self.text = text
        self.length = length
    
    def spaces_text(self, line, spaces):
        output_line = ''
        spaces_received = line.count(' ')
        words = line.split(' ')
        spaces_to_include = spaces_received + spaces
        i = 0
        
        # se retira de la lista los elementos vacios
        for index in range(len(words)):
            if words[index] == '':
                words.pop(index)

        # se insertan espacios uno a uno
        while i < spaces_to_include:
            for j in range(len(words)):
                if words[j] != words[-1]:
                    words[j] += ' '
                    i += 1
                if i == spaces_to_include:
                    break
            
            # para palabras muy largas se corta la longitud dada 
            if spaces_to_include == self.length:
                output_line = self.text[:self.length]
                break
            else:
                output_line = ''.join(words)          

        return output_line
    
    def format_words(self):
        words = self.text.split(' ')
        output_text = ''
        line = ''
        count_words = 0
        len_words_list = len(words)

        # se divite texto en una lista y suma palabras y espacios
        for word in words:
            word_len = len(word)
            temp_sum = len(line) + word_len 
            line_len = len(line)
            
            
            if line_len < self.length:

                # cuando la suma temporal de las palabras es mayor de la longitud dada    
                if temp_sum > self.length:
                    spaces = self.length - line_len
                    formated_line = self.spaces_text(line, spaces)
                    output_text += formated_line + '\n'
                    line = ''
                    line += word + ' '
                elif temp_sum == self.length:
                    line += word
                    formated_line = self.spaces_text(line, 0)
                    output_text += formated_line + '\n'
                    line = ''
                    line += word + ' '
                else:
                    line += word + ' '
                    # para generar la ultima linea
                    if count_words == (len_words_list - 1):
                        line = line[:-1]
                        output_text += line + '\n'
            
            # en casos donde la linea ya tiene una logitud dada
            elif line_len == self.length:
                formated_line = self.spaces_text(line, 0)
                output_text += formated_line + '\n'
                line = ''
                if temp_sum > self.length:
                    line += word + ' '
            
            count_words += 1
            
        return output_text

input_text = 'La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera.'
obj = JustifyText(input_text,30)

print(obj.format_words())

