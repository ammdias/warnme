��    :      �  O   �      �  �
  �  &   �  $   	     .     H     X     a     g     m     ~  
   �     �     �      �     �     �  �  �    �     �     �     �     �     �  G   �     ;     H     U  	   n     x     �     �     �  
   �     �     �     �  	   �     �     �  *        =  #   \     �  &   �  '   �  (   �           0     6      P     q     �     �     �     �     �     �       �  !  -   �,  +   
-     6-     Q-     a-     j-     q-     w-     �-     �-     �-     �-  #   �-     �-     �-  �  �-  4  z3     �:     �:  	   �:     �:     �:  M   �:     @;     O;     ^;     y;  
   �;     �;     �;     �;  	   �;     �;     �;     �;  	   �;  8   �;     !<  =   A<  7   <  :   �<     �<  *   =  ,   9=  -   f=     �=     �=     �=     �=     �=     �=     >  !   !>     C>     `>     r>     2                   %               +      :   5      /       4           3   )   "   *   9                           8      0                           	   
                       6   &                    $       #              '   !      (   7   -      .          1             ,    
Warn me

Copyright (C) 2012 António Manuel Dias
contact: ammdias@gmail.com

This program comes with ABSOLUTELY NO WARRANTY;  for details use command
'warnme.py --warranty' or go to 'Help > Warranty' on the graphical user
interface.

This is free software, and you are welcome to redistribute it under certain
conditions; use command 'warnme.py --copyright' or go to 'Help > Copyright' on
the graphical user interface for details.

----

Warn me is a program to set timed desktop notifications.  It may be used from
the command line if the POSIX 'at' and the freedesktop.org 'notify-send'
utilities are available.  If not or if you prefer to use a graphical interface
the program may be used that way with no other dependencies except Python 3
with Tkinter module.


Graphical User Interface
========================

The program's graphical user interface may be launched in the following ways:

* Launch the 'gwarnme.py' program;
* Launch the 'warnme.py' program with the '--gui' option;
* Trying to use the 'warnme.py' program in a system without either the POSIX
  'at' or the freedesktop.org 'notify-send' utilities.

You may set an alarm in one of these ways:

* Set alarm to fire in a specified interval in minutes:
  - click "Set alarm in"
  - choose the number of minutes
  - type the desired alarm notification message
  - if you wish, set the recurrence interval of the alarm, in minutes
  - press "Set alarm" button

* Set alarm to fire at specified time:
  - click "Set alarm at"
  - choose the hour and minute
  - type the desired alarm notification message
  - if you wish, set the recurrence interval of the alarm, in minutes
  - press "Set Alarm" button

To remove an alarm, select it on the list of pending alarms and press the
"Remove alarm" button.  You may select several alarms simultaneously.

All notifications will be lost if you close the program.

Command Line Interface
======================

Command line interface (terminal) accepted commands and syntax.

* Set alarm at specified interval in minutes:
  $ warnme --in <minutes> [--text <message>]

* Set alarm at specific time:
  $ warnme --at <hour:minute> [--text <message>]

* For each of the previous commands, you may also set the recurrence of the
  alarms, in minutes:
  $ warnme --in <minutes> [--text <message>] --repeat <minutes>
  $ warnme --at <hour:minute> [--text <message>] --repeat <minutes>

* Show list of alarm IDs and descriptions:
  $ warnme --list
  
* Remove alarm identified by alarm ID:
  $ warnme --delete <alarm ID>

* Start the graphical user interface:
  $ warnme --gui

* Print Help, Warranty, Copyright and version information on the terminal:
  $ warnme --help
  $ warnme --warranty
  $ warnme --copyright
  $ warnme --version
  
* Uninstall application:
  $ warnme --uninstall
 'at/atq/atrm' utilities not available. 'notify-send' utility not available. , repeat every %d minutes <Control-Key-q> <Key-F1> ALARM About Alarm not found. Alarm removed. Alarm set: CTRL+Q Close Conflicting options: '--at/--in' Error: F1 From the GNU General Public License:
    
15. Disclaimer of Warranty.

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE
COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS"
WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING,
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY
AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE PROGRAM PROVE
DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
CORRECTION.

16. Limitation of Liability.

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR
CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES
ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT
NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES
SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO
OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY
HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
 From the Preamble of the GNU General Public License:
        
The GNU General Public License is a free, copyleft license for
software and other kinds of works.

The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

See the file LICENSE on the program's directory for more details.
If it's missing please refer to http://www.gnu.org/licenses/gpl.txt
 HH:MM MINUTES Message: Notification text. Pending alarms: Proceeding in stand-alone mode:
closing the GUI will delete all alarms. Remove alarm Repeat every Repeat every {} minutes. Set alarm Set alarm at Set alarm in Standard notification _About _Copyright _Help _Manual _Quit _Warranty cannot create alarm list file. corrupted alarm list file. could not append alarm to alarm list file. could not parse 'at' response. could not write to alarm list file. delete alarm by index. error running 'at' command. Reason:
{} error running 'atq' command. Reason:
{} error running 'atrm' command. Reason:
{} hour and minute for the warning. hours interval for the warning. launch graphical user interface. list set alarms. minutes repeat interval. show copyright information. show version information. show warranty information. uninstall application. Project-Id-Version: 2.3
PO-Revision-Date: 2023-12-07 16:30+0000
Last-Translator: António Manuel Dias <ammdias@gmail.com>
Language-Team: pt_PT <ammdias>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
 
Warn me

Copyright (C) 2012 António Manuel Dias
contacto: ammdias@gmail.com

Este programa é distribuído SEM QUALQUER GARANTIA;  para mais detalhes use o
comando 'warnme.py --warranty' ou use 'Ajuda > Garantia' na interface
gráfica.

Este programa é software livre e pode ser redistribuído sob determinadas
condições;  use o comando 'warnme.py --copyright' ou use 'Ajuda > Licença'
na interface gráfica para mais detalhes.

----

Warn me é um programa para mostrar notificações temporizadas no ambiente de
trabalho.  Pode ser usado a partir da linha de comando em ambientes onde os
utilitários 'at' (POSIX) e 'notify-send' (freedesktop.org) estejam
disponíveis.  Em caso contrário, ou se preferir usar uma interface gráfica,
o programa pode ser usado dessa forma sem nenhuma dependência para além de
Python 3 com o módulo Tkinter.


Interface Gráfica
=================

A interface gráfica pode ser iniciada das seguintes formas:

* Correr o programa 'gwarme.py';
* Correr o programa 'warnme.py' com a opção '--gui';
* Tentar correr o programa 'warnme.py' num sistema sem qualquer um dos
  utilitários 'at' (POSIX) ou 'notify-send' (freedesktop.org).

Para programar um alarme, use uma das seguintes formas:

* Programar um alarme para um determinado intervalo em minutos:
  - clicar "Alarme daqui a"
  - escolher o número de minutos
  - escrever a mensagem de notificação desejada
  - se desejar, programar a recorrência do alarme, em minutos
  - clicar o botão "Ativar alarme"

* Programar alarme para uma determinada hora:
  - clicar "Alarme às"
  - escolher a hora e minuto
  - escrever a mensagem de notificação desejada
  - se desejar, programar a recorrência do alarme, em minutos
  - clicar o botão "Ativar alarme"

Para remover um alarme, selecione-o na lista de alarmes pendentes e clique
o botão "Remover alarme".  Pode selecionar vários alarmes em simultâneo.

Ao fechar o programa, todas as notificações serão removidas.

Interface de Linha de Comando
=============================

Comandos da interface de linha de comando (terminal) e sua sintaxe:

* Programar um alarme para um determinado intervalo, em minutos:
  $ warnme --in <minutos> [--text <mensagem>]

* Programar um alarme para uma determinada hora:
  $ warnme --at <hora:minuto> [--text <mensagem>]

* Para cada um dos comandos anteriores, pode também programar a recorrência
  dos alarmes, em minutos:
  $ warnme --in <minutos> [--text <mensagem>] --repeat <minutos>
  $ warnme --at <hora:minuto> [--text <mensagem>] --repeat <minutos>

* Mostrar a lista dos identificadores (ID) dos alarmes e suas descrições:
  $ warnme --list
  
* Remover alarme identificado pelo seu identificador:
  $ warnme --delete <ID do alarme>

* Iniciar a interface gráfica:
  $ warnme --gui

* Mostrar informação sobre a Ajuda, Garantia, Licença e versão no terminal:
  $ warnme --help
  $ warnme --warranty
  $ warnme --copyright
  $ warnme --version
  
* Desinstalar aplicação:
  $ warnme --uninstall
 Utilitários 'at/atq/atrm' não disponíveis. Utilitário 'notify-send' não disponível. , repete a cada %d minutos <Control-Key-q> <Key-F1> ALARME Sobre Alarme não encontrado. Alarme removido. Alarme configurado: CTRL+Q Fechar Opções conflituantes: '--at/--in' Erro: F1 Da Licença Pública Geral GNU:

15. Exclusão de Garantia.

NÃO HÁ QUALQUER GARANTIA PARA O PROGRAMA, NO LIMITE PERMITIDO PELA LEI
APLICÁVEL.  EXCEPTO QUANDO DE OUTRA FORMA ESTABELECIDO POR ESCRITO, OS
TITULARES DOS DIREITOS DE AUTOR E/OU OUTRAS PARTES, FORNECEM O PROGRAMA
"COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, TANTO EXPRESSA COMO
IMPLÍCITA, INCLUINDO, ENTRE OUTRAS, AS GARANTIAS IMPLÍCITAS DE
COMERCIABILIDADE E ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. O RISCO QUANTO
À QUALIDADE E DESEMPENHO DO PROGRAMA É SEU. CASO O PROGRAMA CONTENHA
DEFEITOS, O UTILIZADOR ARCARÁ COM OS CUSTOS DE TODOS OS SERVIÇOS,
REPARAÇÕES OU CORREÇÕES NECESSÁRIAS.

16. Limites de Responsabilidade.

EM NENHUMA CIRCUNSTÂNCIA, A MENOS QUE EXIGIDO PELA LEI APLICÁVEL OU SEJA
ACORDADO POR ESCRITO, QUALQUER TITULAR DE DIREITOS DE AUTOR OU QUALQUER
OUTRA PARTE QUE ALTERE E/OU FORNEÇA O PROGRAMA CONFORME PERMITIDO ACIMA,
SERÁ RESPONSÁVEL PELOS DANOS DO UTILZIADOR, INCLUINDO ENTRE OUTROS,
QUAISQUER DANOS GERAIS, ESPECIAIS, FORTUITOS OU EMERGENTES, RESULTANTES
DO USO OU IMPOSSIBILIDADE DE USO DO PROGRAMA (INCLUINDO, ENTRE OUTROS,
PERDAS DE DADOS OU DADOS GERADOS DE FORMA IMPRECISA, PERDAS SOFRIDAS
PELO UTILIZADOR OU TERCEIROS OU A IMPOSSIBILIDADE DO PROGRAMA DE OPERAR
COM QUAISQUER OUTROS PROGRAMAS), MESMO QUE ESSE TITULAR OU OUTRA PARTE,
TENHA SIDO ALERTADA SOBRE A POSSIBILIDADE DE OCORRÊNCIA DESSES DANOS.
 Do Preâmbulo da Licença Pública Geral GNU:
        
A Licença Pública Geral GNU é uma licença livre para software e outros
tipos de trabalhos.

As licenças da maioria do software e outros trabalhos práticos são
elaboradas de forma a suprimir a liberdade de os partilhar e modificar.
Pelo contrário, a Licença Pública Geral GNU visa garantir a liberdade
de partilhar e modificar todas as versões de um programa para assegurar
que o software permaneça livre para todos os seus utilizadores.  Nós, na
Free Software Foundation, usamos a Licença Pública Geral GNU para a maioria
do nosso software; também se aplica a qualquer outra obra distribuída desta
forma pelos seus autores.  Pode aplicá-la igualmente aos seus programas.

Quando falamos de software livre referimo-nos à liberdade, não ao preço.
As nossas Licenças Públicas Gerais visam garantir-lhe a liberdade de
distribuir cópias de software livre (e cobrar por isso se desejar), que
receba o código-fonte ou o possa obter se desejar, que o possa modificar
ou usar partes dele em novos programas livres; e que esteja ciente de que
o pode fazer.

Para proteger os seus direitos necessitamos de evitar que alguém lhos negue
ou solicite que lhes renuncie.  Assim, tem determinadas responsabilidades
no caso de distribuir cópias do software ou se o modificar.

Por exemplo, se distribuir cópias de um programa assim licenciado, seja
gratuitamente ou mediante pagamento, terá de conceder aos receptores os
direitos que possui.  Terá de garantir que, também eles, recebam ou possam
obter o código-fonte.  E terá a obrigação de lhes mostrar estes termos,
para que conheçam os seus direitos.

Consulte o ficheiro 'gpl.txt' na directoria do programa para mais detalhes.
Se não o encontrar, por favor consulte a licença em
http://www.gnu.org/licenses/gpl.txt
 HH:MM MINUTOS Mensagem: Texto da notificação. Alarmes pendentes: Prosseguindo em modo autónomo:
fechar o programa removerá todos os alarmes. Remover alarme Repetir a cada Repetir a cada {} minutos. Activar alarme Alarme às Alarme daqui a Notificação padrão _Sobre _Licença _Ajuda _Manual Sai_r _Garantia não foi possível criar o ficheiro da lista de alarmes. ficheiro de alarmes corrompido. não foi possível adicionar o alarme ao ficheiro de alarmes. não foi possível processar resposta do programa 'at'. não foi possível guardar o ficheiro da lista de alarmes. remover alarme por índice. erro ao executar o comando 'at'. Motivo
{} erro ao executar o comando 'atq'. Motivo:
{} erro ao executar o comando 'atrm'. Motivo:
{} hora e minuto do alarme. horas intervalo para o alarme. lançar interface gráfico. listar alarmes ativos. minutos intervalo de repetição. mostrar licença de utilização. mostrar versão do programa. mostrar garantia. desinstalar aplicação. 