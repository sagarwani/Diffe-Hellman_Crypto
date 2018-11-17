Implementation of Diffie-Hellman key exchange protocol at a 1024-bit key strength.

The first models Alice's initial message to Bob, and outputs a secret key to be stored for later. The second models Bob's receipt of the message from Alice, and outputs a response message back to Alice. The final program models Alice's receipt of Bob's response.

dh-alice1 <filename for message to Bob> <filename to store secret key>.
Outputs decimal-formatted ( p; g; ga ) to Bob, writes (p; g; a) to a second file.
dh-bob <filename of message from Alice> <filename of message back to Alice>.
Reads in Alice's message, outputs ( gb ) to Alice, prints the shared secret gab.
dh-alice2 <filename of message from Bob> <filename to read secret key>.
Reads in Bob's message and Alice's stored secret, prints the shared secret gab.
