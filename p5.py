import math

def seno(x):
  #dentro da variável x será passado um números real (float)
  #a função deve retornar o seno de x, usando a a série de Taylor até o termo de grau 7 (x⁷), veja aqui a série http://people.math.sc.edu/girardi/m142/handouts/10sTaylorPolySeries.pdf
  #você pode usar qualquer função da biblioteca math para resolver o problema, usar o math.sin foge ao propósito do problema!
  #tente achar algum truque para que mesmo usando termos até x⁷ sua função consiga ser precisa para números maiores que 2*pi, fica a dica que a função é periódica e para todo número do tipo x, se x>2*pi, esse x pode ser escrito como 2*pi*k+q onde k é um número inteiro e 0<=q<2*pi  
  
  #coloque o seu codigo nesse espaço
  
  
  return 0 # mude para sua resposta aqui

#alguns testes para facilitar a vida, tudo deve retornar True quando seu código funcionar
print(0.1>abs(math.sin(0)-seno(0)))
print(0.1>abs(math.sin(1)-seno(1)))
print(0.1>abs(math.sin(2)-seno(2)))
print(0.1>abs(math.sin(3)-seno(3)))
print(0.1>abs(math.sin(4)-seno(4)))
print(0.1>abs(math.sin(5)-seno(5)))
print(0.1>abs(math.sin(6)-seno(6)))


print(0.1>abs(math.sin(100)-seno(100)))
print(0.1>abs(math.sin(10000)-seno(10000)))
