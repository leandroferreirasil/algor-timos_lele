programa
{
	inclua biblioteca Matematica
	//Algoritmo para calcular média e imprimir o nome do aluno
	funcao inicio()
	{
	cadeia nome 
	real nota_1, nota_2, nota_3, nota_4, media

	escreva("Digite o nome do aluno: ")
	leia (nome)

	escreva("\nDigite a primeira nota: ")
	leia(nota_1)
	escreva("\nDigite a primeira nota: ")
	leia(nota_2)
	escreva("\nDigite a primeira nota: ")
	leia(nota_3)
	escreva("\nDigite a primeira nota: ")
	leia(nota_4)

	media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
	escreva ("O aluno: ", nome, " ficou com média: ", media)

	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 551; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */