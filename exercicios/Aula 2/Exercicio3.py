#--- Exercicio 3  - Variávies e impressão com interpolacão de string
#--- Imprima dois paragráfos do ultimo livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- Livro: Título, Edição, Autor, Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

Titulo = ('The Tangled Web: A Guide to Securing Modern Web Applications')
Edicao = ('2012')
Autor = ('Michał Zalewski')
Publicacao = ('Primeira edição: Novembro de 2011')
Texto = ('\nInformation Security in a Nutshell.\n \n \tOn the face of it, the field of information security appears to be a mature, well-defined, and accomplished branch of computer science. Resident experts eagerly assert the importance of \n \ttheir area of expertise by pointing to large sets of neatly cataloged security flaws, invariably attributed to security-illiterate developers, while their fellow theoreticians note how all\n \tthese problems would have been prevented by adhering to this year’s hottest security methodology.\n \n2 Chapter 1\n \n\tA commercial industry thrives in the vicinity, offering various nonbinding security assurances to everyone, from casual computer users to giant international corporations.\n \tYet, for several decades, we have in essence completely failed to come up with even the most rudimentary usable frameworks for understanding and assessing the security of modern software.\n \tSave for several brilliant treatises and limited-scale experiments, we do not even have any real-world success stories to share. The focus is almost exclusively on reactive, secondary secu-\n \trity measures (such as vulnerability management, malware and attack detection, sandboxing, and so forth) and perhaps on selectively pointing out flaws in somebody else’s code. The frustra-\n \tting, jealously guarded secret is that when it comes to enabling others to develop secure systems, we deliver far less value than should be expected; the modern Web is no exception. Let’s \n\tlook at some of the most alluring approaches to ensuring information security and try to figure out why they have not made a difference so far.')

print(f'\nTitulo: {Titulo} \nAutor: {Autor} \nEdição: {Edicao} \nPublicação: {Publicacao}\n \nPrévia:\n {Texto}\n')
