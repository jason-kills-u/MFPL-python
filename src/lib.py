ADD, SUB, OUT, IN, DONE, MOVL, MOVR = 0, 1, 2, 3, 4, 5, 6

class Interpreter(object):
	def __init__(self, text):
		self.text = text
		self.pos = 0
		self.current_char = self.text[self.pos]
	def parsing_error(self, msg):
		raise Exception(msg)
	def advance(self):
		self.pos += 1 
		if self.pos > len(self.text) - 1:
			self.current_char = None 
		else:
			self.current_char = self.text[self.pos]
	def skip_newline(self):
		while self.current_char is not None and self.current_char == '\n':
			self.advance()
	def skip_whitespace(self):
		while self.current_char is not None and self.current_char == ' ':
			self.advance()
	def skip_tab(self):
		while self.current_char is not None and self.current_char == '\t':
			self.advance()
	def statement(self):
		result = ''
		while self.current_char is not None and self.current_char.isalpha():
			result += self.current_char
			self.advance()
		return result
	def get_ir(self):
		statements = []
		while self.current_char is not None:
			if self.current_char.isalpha():
				current_statement = self.statement()
				if current_statement == 'add':
					statements.append(ADD)
				elif current_statement == 'sub':
					statements.append(SUB)
				elif current_statement == 'out':
					statements.append(OUT)
				elif current_statement == 'in':
					statements.append(IN)
				elif current_statement == 'done':
					statements.append(DONE)
				elif current_statement == 'movl':
					statements.append(MOVL)
				elif current_statement == 'movr':
					statements.append(MOVR)
				else:
					self.parsing_error('Unexpected statement {}'.format(current_statement))
			elif self.current_char == '\n':
				self.skip_newline()
				continue
			elif self.current_char == ' ':
				self.skip_whitespace()
				continue
			elif self.current_char == '\t':
				self.skip_tab()
				continue
			else:
				self.parsing_error("Unexpected character {}".format(self.current_char))
		return statements
	def interpret(self):
		i = 0
		tapeCounter = 0
		tape = [65] * 30000
		for i in self.get_ir():
			if i == ADD:
				tape[tapeCounter] += 1
			elif i == SUB:
				tape[tapeCounter] -= 1
			elif i == MOVL:
				tapeCounter += 1
			elif i == MOVR:
				tapeCounter -= 1
			elif i == OUT:
				# debug!
				print(chr(tape[tapeCounter]), end = '')
				#pass
			elif i == IN:
				tape[tapeCounter] = ord(input())
			elif i == DONE:
				break
			else:
				self.parsing_error('Unexpected statement {}'.format(i))
		if i != DONE:
			self.parsing_error('Expected \"done\" at EOF')
		print('')
