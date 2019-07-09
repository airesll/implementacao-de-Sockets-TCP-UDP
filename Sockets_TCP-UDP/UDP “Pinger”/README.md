# UDP �Pinger�
## Envio e recebimento de pacotes datagramas usando soquetes UDP, definindo um tempo limite (�timeout�) de soquete apropriado.
* A funcionalidade fornecida pelo
cliente e servidor em Python � semelhante � fornecida pelos programas de
Ping dispon�veis nos sistemas operacionais modernos. No entanto, eles
(cliente e servidor) usam um protocolo mais simples, o UDP, em vez do
protocolo ICMP (Internet Control Message Protocol) para se comunicar entre
si. O protocolo ping permite que uma m�quina cliente envie um pacote de
dados para uma m�quina remota e fa�a com que a m�quina remota retorne
os dados inalterados de volta ao cliente (uma a��o chamada de �eco�).
Entre outros usos, o protocolo ping permite que os hosts determinem
tempos de ida e volta (Round-Trip Time ou RTT) para outras m�quinas.