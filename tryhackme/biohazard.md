Gonna wait a few minutes for everything to boot up properly... []

[surprisingly I only got stuck at crest 1 because what the fuck?]


IP=10.10.121.78

Found 3 ports:

* 21 - ftp
* 22 - ssh
* 80 - http

```
PATH:

/teaRoom
/artRoom
/barRoom
/diningRoom
/diningRoom2F
/tigerStatusRoom
/galleryRoom
/studyRoom (???)
/armorRoom
/attic
/studyRoom
/hidden_closet

```

potential-usernames: {Chris, Jill, Barry, Weasker, Joseph} [kinda-helped?]

SG93IGFib3V0IHRoZSAvdGVhUm9vbS8= (base64) >> teaRoom
emblem{fec832623ea498e20bf4fe1821d58727} [???] [Used at barRoomHidden!] >> {rebecca} [???] [Used as key for the vigenere]
lock_pick{037b35e2ff90916a9abf99129c8e1837} [???] [Used at /barRoom!]

/artRoom/MansionMap.html:

```
Look like a map

Location:
/diningRoom/
/teaRoom/
/artRoom/
/barRoom/
/diningRoom2F/
/tigerStatusRoom/
/galleryRoom/
/studyRoom/
/armorRoom/
/attic/

```

moonlight somata:

```
Look like a music note
NV2XG2LDL5ZWQZLFOR5TGNRSMQ3TEZDFMFTDMNLGGVRGIYZWGNSGCZLDMU3GCMLGGY3TMZL5 

```

NV2XG2LDL5ZWQZLFOR5TGNRSMQ3TEZDFMFTDMNLGGVRGIYZWGNSGCZLDMU3GCMLGGY3TMZL5 (base32) >> music_sheet{362d72deaf65f5bdc63daece6a1f676e} [Used to play the piano ...]

gold_emblem{58a8c41a9d08b8a4e38d02a4d7ff4843} [???] [Used at /dinningRoom] >> {
    klfvg ks r wimgnd biz mpuiui ulg fiemok tqod. Xii jvmc tbkg ks tempgf tyi_hvgct_jljinf_kvc
    (vigenere cipher - keyword: rebecca)
    THERE IS A SHIELD KEY INSIDE THE DINING ROOM. THE HTML PAGE IS CALLED THE_GREAT_SHIELD_KEY
}   

the_great_shield_key.html > shield_key{48a7a9227cd7eb89f0a062590798cbac} [???] [Used at /armorRoom!]

at dinningRoom2F source code >> {
    Lbh trg gur oyhr trz ol chfuvat gur fgnghf gb gur ybjre sybbe. Gur trz vf ba gur qvavatEbbz svefg sybbe. Ivfvg fnccuver.ugzy
    (rot_13)
    You get the blue gem by pushing the status to the lower floor. The gem is on the diningRoom first floor. Visit sapphire.html
}

sapphire.html > blue_jewel{e1d457e96cac640f863ec7bc475d48aa} [???] [Used at /tigerStatusRoom!]

from tigerStatusRoom:

```
crest 1:
S0pXRkVVS0pKQkxIVVdTWUpFM0VTUlk9
Hint 1: Crest 1 has been encoded twice
Hint 2: Crest 1 contanis 14 letters
Note: You need to collect all 4 crests, combine and decode to reavel another path
The combination should be crest 1 + crest 2 + crest 3 + crest 4. Also, the combination is a type of encoded base and you need to decode it

```
crest1 >> RlRQIHVzZXI6IG [?]

from galleryRoom:

```
crest 2:
GVFWK5KHK5WTGTCILE4DKY3DNN4GQQRTM5AVCTKE
Hint 1: Crest 2 has been encoded twice
Hint 2: Crest 2 contanis 18 letters
Note: You need to collect all 4 crests, combine and decode to reavel another path
The combination should be crest 1 + crest 2 + crest 3 + crest 4. Also, the combination is a type of encoded base and you need to decode it

```
crest2 >> h1bnRlciwgRlRQIHBh [??]

from armorRoom:

```
crest 3:
MDAxMTAxMTAgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAxMDAgMDExMDAxMDAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMDAgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMDAgMDAxMTEwMDAgMDAxMDAwMDAgMDAxMTAxMTAgMDExMDAwMTEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAxMDAgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMTAgMDExMDAwMDEgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTAxMTEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAxMDEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMDAgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTEwMDAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTEwMDA=
Hint 1: Crest 3 has been encoded three times
Hint 2: Crest 3 contanis 19 letters
Note: You need to collect all 4 crests, combine and decode to reavel another path
The combination should be crest 1 + crest 2 + crest 3 + crest 4. Also, the combination is a type of encoded base and you need to decode it

```
crest3 >> c3M6IHlvdV9jYW50X2h [???]

from attic:

```
crest 4:
gSUERauVpvKzRpyPpuYz66JDmRTbJubaoArM6CAQsnVwte6zF9J4GGYyun3k5qM9ma4s
Hint 1: Crest 2 has been encoded twice
Hint 2: Crest 2 contanis 17 characters
Note: You need to collect all 4 crests, combine and decode to reavel another path
The combination should be crest 1 + crest 2 + crest 3 + crest 4. Also, the combination is a type of encoded base and you need to decode it

```
crest4 >> pZGVfZm9yZXZlcg== [????]


sum(crests)

```
RlRQIHVzZXI6IGh1bnRlciwgRlRQIHBhc3M6IHlvdV9jYW50X2hpZGVfZm9yZXZlcg==
(base64)
FTP user: hunter, FTP pass: you_cant_hide_forever

```

woot... log to ftp, grab the files to a local directory and start working on it...

```
$ cat important.txt 
Jill,

I think the helmet key is inside the text file, but I have no clue on decrypting stuff. Also, I come across a /hidden_closet/ door but it was locked.

From,
Barry

```

use stegseek on the 001-key.jpg, finds:

001 >> cGxhbnQ0Ml9jYW

both stegseek and binwalk can't find anything out of 002-key.jpg, will try later [???]

binwalk finds something at 003-key.jpg, at the output folder there is a .txt document and a zip:

003 >> 3aXRoX3Zqb2x0

oops .. extracting the zip is the .txt file .. whatever

back to 002-key.jpg, finds the comment "5fYmVfZGVzdHJveV9" with exiftools (duh...)

cGxhbnQ0Ml9jYW5fYmVfZGVzdHJveV93aXRoX3Zqb2x0 (base64) >> plant42_can_be_destroy_with_vjolt [???] [wtf?] [Used as the key for the .gpg]

moving on to the .gpg file, reading around the man pages there is --decrypt argument

gpg --decrypt "helmet_key.txt.gpg", enter key `plant42_can_be_destroy_with_vjolt`

helmet_key{458493193501d2b94bbab2e727f8db4b} [Pretty clear...]

from /studyRoom >> SSH user: umbrella_guest

from /hidden_closet/

```
    SSH password: T_virus_rules,
    wpbwbxr wpkzg pltwnhro, txrks_xfqsxrd_bvv_fy_rvmexa_ajk [???] [Key is `albert`]

```

connecting via ssh

ls -la

.jailcell?

```
Jill: Chris, is that you?
Chris: Jill, you finally come. I was locked in the Jail cell for a while. It seem that weasker is behind all this.
Jil, What? Weasker? He is the traitor?
Chris: Yes, Jill. Unfortunately, he play us like a damn fiddle.
Jill: Let's get out of here first, I have contact brad for helicopter support.
Chris: Thanks Jill, here, take this MO Disk 2 with you. It look like the key to decipher something.
Jill: Alright, I will deal with him later.
Chris: see ya.

MO disk 2: albert

```

WEASKER LOGIN PASSWORD, STARS_MEMBERS_ARE_MY_GUINEA_PIG

moving to weasker user

```
Weaker: Finally, you are here, Jill.
Jill: Weasker! stop it, You are destroying the  mankind.
Weasker: Destroying the mankind? How about creating a 'new' mankind. A world, only the strong can survive.
Jill: This is insane.
Weasker: Let me show you the ultimate lifeform, the Tyrant.

(Tyrant jump out and kill Weasker instantly)
(Jill able to stun the tyrant will a few powerful magnum round)

Alarm: Warning! warning! Self-detruct sequence has been activated. All personal, please evacuate immediately. (Repeat)
Jill: Poor bastard

```

sudo -l >> (ALL : ALL) oh .. ok

sudo cat /root/root.txt [GG]

```
In the state of emergency, Jill, Barry and Chris are reaching the helipad and awaiting for the helicopter support.

Suddenly, the Tyrant jump out from nowhere. After a tough fight, brad, throw a rocket launcher on the helipad. Without thinking twice, Jill pick up the launcher and fire at the Tyrant.

The Tyrant shredded into pieces and the Mansion was blowed. The survivor able to escape with the helicopter and prepare for their next fight.

The End

flag: 3c5794a00dc56c35f2bf096571edf3bf

```
