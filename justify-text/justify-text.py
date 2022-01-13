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
        

input_text = 'La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera.'
obj = JustifyText(input_text,30)

print(obj.format_text(input_text))

