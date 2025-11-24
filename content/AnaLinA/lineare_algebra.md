# Lineare Algebra

## Lineare Abbildungen

### Linearität

Es seien V1 und V2 zwei Vektorräume. Eine Abbildung $f: V_1 \longrightarrow V_2$ heißt *linear*, falls für alle Vektoren
$u,v \in V_1$ und für jedes $\lambda \in \mathbb{R}$ gilt:

> (1) Additivität: $f(u+v) = f(u) + f(v)$
>
> (2) Homogenität: $f(\lambda u) = \lambda f(u)$

**Beweisschema**:

1. Festlegung beliebiger Elemente aus dem Definitionsbereich: *Seien $u, v \in V$ beliebige Vektoren und sei $\lambda \in K$ ein beliebiger Skalar.*
2. Nachweis der Additivität: *zusammenfassen $\rightarrow$ anwenden $\rightarrow$ sortieren $\rightarrow$ trennen*
    - Vektoren im Argument der Funktion addieren
    - $f(u+v)$ so lange umformen, bis $f(u)+f(v)$ entsteht (Distributiv-/Kommutativgesetze)
3. Nachweis der Homogenität: 
    - $f(\lambda u)$ umformen, bis $\lambda f(u)$ entsteht
    - Multiplikation im Argument ausführen
    - Abbildungsvorschrift anwenden

> Es ist **keine** lineare Abbildung, wenn:
> - Konstanten ohne Variable vorkommen (z.B. $2x+5$)
> - Potenzen vorkommen ($x^2, x^3, \sqrt(x)$)
> - Produkte von Variablen vorkommen ($x\cdot y$); aber Produkte mit Zahlen sind in Ordnung!
> - Funktionen wie $\sin(x), e^x, ln(x)$ vorkommen


### Bild und Kern 

Zwei wichtige Mengen (bei der Betrachtung linearer Abbildungen) sind das **Bild** und der **Kern**.

Sei $f: V \longrightarrow W$ linear.

- Der Kern von f ist das Urbild von 0; $Kern(f)$ ist ein Teilraum von $V$
$$Kern(f) = \\{v \in V \mid f(v)=0\\} = f^{-1}(\\{0\\})$$
$\Rightarrow$ *die Menge aller Vektoren aus dem Definitionsbereich $V$, die auf den Nullvektor des Zielraums $W$ abgebildet werden*

> Der Kern besteht aus allen Vektoren, die auf den Nullvektor abgebildet werden: $Ax=0$. *Ansatz: homogenes Gleichungssystem lösen:* [Matrix A | 0]

- Das Bild von f ist die Menge; $Bild(f)$ ist ein Teilraum von $W$
$$Bild(f) = f(V) = \\{f(v) \mid v \in V\\}$$
$\Rightarrow$ *die Menge aller Vektoren im Zielraum $W$, die ein Urbild in $V$ besitzen*

> Die Spalten der Matrix anschauen. Spaltenvektoren von A, die zu einem Pivotelement in ZSF gehören, bilden eine Basis des Bildes. $\rightarrow dim(Bild(A))=Rang(A)$

### Dimensionsformel (Injektivität / Surjektivität)

**Folgerungen aus der Dimensionsformel:**
Sei $f: V \rightarrow W$ linear. Dann gilt:
> (1) f ist **injektiv** $\Leftrightarrow A\vec x = \vec 0 \Leftrightarrow Kern(f) = \\{0\\} \Leftrightarrow dim(Kern(f))=0$ 
> 
> (2) f ist **surjektiv** $\Leftrightarrow Bild(f) = W \Leftrightarrow dim(Bild(f))=dim(W)$
> 
> (3) wenn $dim(V) = dim(W) < \infty$, so gilt: f ist bijektiv $\Leftrightarrow$ f ist injektiv $\Leftrightarrow$ f ist surjektiv

- Eine lineare Abbildung ist genau dann `injektiv`, wenn der Kern nur den *Nullvektor* enthält ($Kern(f)=\\{0\\}$). 
- Eine Abbildung ist `surjektiv`, wenn das Bild den *gesamten Zielraum* abdeckt. Wir nutzen die **Dimensionsformel**:

$$dim(V)=dim(Kern(f))+dim(Bild(f))$$
