class JustifyText():
    
    def __init__(self, text, length):
        self.text = text
        self.length = length
    
    def format_text(self, text):
        output_text = ''
        count_char = 0
        line = ''

        for j in text:
            if count_char != 0:
                line = count_char % self.length
            
            if line == 0:
                output_text += '\n'+j
            else:
                output_text += j
            
            count_char += 1

        return output_text

    
    def format_words(self):
        words = self.text.split(' ')
        output_text = ''
        count_char = 0
        line = ''
        len_text = len(self.text)
        count_line = 0

        for word in words:
            word_len = len(word) # 6
            temp_sum = len(line) + word_len # 24 + 6 =31
            line_len = len(line)
            

            if line_len < self.length:
                #print(line_len)
                if temp_sum > self.length: # 31 < 30
                    spaces = self.length - line_len
                    output_text += line + spaces * '*' + '\n'
                    line = ''
                    line += word + '#'
                elif temp_sum == self.length:
                    line += word
                    output_text += line + '\n'
                    line = ''
                    line += word + '#'
                else:
                    line += word + '#' # 2
                    if word == words[-1]:
                        line = line[:-1]
                        output_text += line
            
            elif line_len == self.length:
                output_text += line + '\n'
                line = ''
                if temp_sum > self.length:
                    line += word + '#'

            
        return output_text

input_text = 'La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera.'
obj = JustifyText(input_text,30)

print(obj.format_words())

