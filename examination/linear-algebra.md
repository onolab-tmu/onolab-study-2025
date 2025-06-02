## 線形代数 確認テスト

### 表記

本資料では特に表記しない限り，行列を $A$, $B$ のように大文字斜体で表記し，ベクトルを $\boldsymbol{x}, \boldsymbol{y}$ のように小文字斜体太字で表記する．
行列・ベクトルの要素は複素数とする．
行列・ベクトルの転置を $A^{\top}, \boldsymbol{v}^{\top}$ で表記し， Hermite 転置を $A^{\mathsf{H}}, \boldsymbol{v}^{\mathsf{H}}$ で表記する．
複素数 $x$ に対してその複素共役を $x^{\ast}$ で表記する．
また，行列の次元は $N\times N$ 次元とし，

$$
A = \begin{bmatrix} a_{11} & \cdots & a_{1N} \\ \vdots & \ddots & \vdots \\ a_{N1} & \cdots & a_{NN} \end{bmatrix}
$$

のようにその $i$ 行 $j$ 列の要素を $a_{ij}\quad (i, j = 1, \dots, N)$ と表記する．
ベクトルも同様に

$$
\boldsymbol{x} = \begin{bmatrix} x_{1} \\ \vdots \\ x_{N}\end{bmatrix}
$$

のようにその $i$ 番目の要素を $x_{i}\quad (i = 1, \dots, N)$ と表記する．

### 問題

- 2 個の $N$ 次元ベクトル $\boldsymbol{x}, \boldsymbol{y}$ に対して，それらの内積 $\boldsymbol{x} ^{\mathsf{H}} \boldsymbol{y}$ の定義を $x_{i}, y_{i}\quad (i = 1, \dots, N)$ を用いて答えよ．また，その計算量をオーダー表記で答えよ．
  <div style="height: 5em;"></div>
- 2 個の $N$ 次元ベクトル $\boldsymbol{x}, \boldsymbol{y}$ に対して，それらの外積 $\boldsymbol{x} \boldsymbol{y} ^{\mathsf{H}}$ の定義を $x_{i}, y_{i}\quad (i = 1, \dots, N)$ を用いて答えよ．また，その計算量をオーダー表記で答えよ．
  <div style="height: 5em;"></div>
- $N$ 次正方行列 $A$ と $N$ 次元ベクトル $\boldsymbol{x}$ に対して，それらの乗算 $A \boldsymbol{x}$ の定義を $a_{ij}, x_{i}\quad (i, j = 1, \dots, N)$ を用いて答えよ．また，その計算量をオーダー表記で答えよ．
  <div style="height: 5em;"></div>
- $N$ 次正方行列 $A$ と $N$ 次元ベクトル $\boldsymbol{x}$ に対して，2 次形式 $ \boldsymbol{x} ^{\mathsf{H}} A \boldsymbol{x}$ の定義を $a_{ij}, x_{i}\quad (i, j = 1, \dots, N)$ を用いて答えよ．また，その計算量をオーダー表記で答えよ．
  <div style="height: 5em;"></div>
- $N$ 次正方行列 $A$ と $B$ に対して，それらの乗算 $A B$ の定義を $a_{ij}, b_{ij}\quad (i, j = 1, \dots, N)$ を用いて答えよ．また，その計算量をオーダー表記で答えよ．
  <div style="height: 5em;"></div>
- $N$ 個のベクトル $\boldsymbol{a}_1, \boldsymbol{a}_2, \dots, \boldsymbol{a}_N$ に対して，線形従属・線形独立の定義を答えよ．
  <div style="height: 5em;"></div>
- $3$ 個のベクトル $\begin{bmatrix} 1 \\ -1 \\ 0\end{bmatrix}$, $\begin{bmatrix} 1 \\ 1 \\ 0\end{bmatrix}$, $\begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix}$ が線形従属または線形独立であるかを調べよ．
  <div style="height: 10em;"></div>
- $N$ 次正方行列 $A$ に対して，固有値と固有ベクトルの定義を答えよ．
  <div style="height: 4em;"></div>
- 2 次正方行列 $A = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}$ に対して，固有値と固有ベクトルを計算する方法を $a_{ij}\quad (i, j = 1, 2)$ の式で表せ．
  <div style="height: 8em;"></div>
- 2 次正方行列 $A = \begin{bmatrix} 4 & 1 \\ -2 & 1 \end{bmatrix}$ の行列式 $\det A$ と逆行列 $A^{-1}$ を計算せよ．
  <div style="height: 12em;"></div>
- 2 次正方行列 $A = \begin{bmatrix} 4 & 1 \\ -2 & 1 \end{bmatrix}$ に対して，固有値と固有ベクトルを計算し， $A^{n}$（ただし $n$ は整数） を求めよ．
  <div style="height: 12em;"></div>
- $N$ 次正方行列 $A$ の固有値を $\lambda$， 固有ベクトルを $\boldsymbol{v}$ とする． $A ^2$ の固有値が $\lambda ^2$ となることを示せ．
  <div style="height: 10em;"></div>
- $N$ 次 **対称行列** $A$ の固有値を $\lambda$， 固有ベクトルを $\boldsymbol{v}$ とする．以下の小問に答えよ．
  1. $\lambda$ が実数になることを示せ（ヒント: $\boldsymbol{x} ^{\mathsf{H}} \boldsymbol{x} \geq 0$ を示し $\lambda = \lambda ^{\ast}$ を導けばよい）．
  2. $A$ の異なる固有値に対応する固有ベクトルが直交することを示せ．
  3. $A$ が直交行列により対角化できることを示せ．
  <div style="height: 20em;"></div>
- $N$ 次元ベクトル $\boldsymbol{x}$ に対して，
  1. $\lambda$ が実数になることを示せ（ヒント: $\boldsymbol{x} ^{\mathsf{H}} \boldsymbol{x} \geq 0$ を示し $\lambda = \lambda ^{\ast}$ を導けばよい）．
  2. $A$ の異なる固有値に対応する固有ベクトルが直交することを示せ．
  3. $A$ が直交行列により対角化できることを示せ．
  <div style="height: 10em;"></div>
- $N$ 次元行列 $A$ のランクの定義を答えよ．
  <div style="height: 10em;"></div>
- 2 個の $N$ 次元ベクトル $\boldsymbol{x}, \boldsymbol{y}$ に対して，$\boldsymbol{x} \boldsymbol{y} ^{\mathsf{H}}$ のランクを求めよ．
  <div style="height: 10em;"></div>
