# Linear Algebra
This project is for learning Linear Algebra concepts. 

---

# Learning Strategy
1. Use AI to  create an Q & A study guide based on questions from schaums guide
2. Work 2 problems on paper and 2 in python for each concept
3. Use a AI to create an exam covering all topics.
4. Get 80% on exam

---

# Table of Contents
- [Concepts to Learn](#concepts-to-learn)
- [Goal](#goal)
- [Linear Algebra Roadmap for LU, QR, and SVD](#linear-algebra-roadmap-for-lu-qr-and-svd)
  - [1. Vectors](#1-vectors)
  - [2. Matrix Operations](#2-matrix-operations)
  - [3. Linear Systems](#3-linear-systems)
- [Geometry of Linear Algebra](#geometry-of-linear-algebra)
  - [4. Linear Transformations](#4-linear-transformations)
  - [5. Basis and Coordinate Systems](#5-basis-and-coordinate-systems)
  - [6. Rank](#6-rank)
  - [7. Column Space and Null Space](#7-column-space-and-null-space)
- [Orthogonality](#orthogonality)
  - [8. Orthogonal Vectors](#8-orthogonal-vectors)
  - [9. Orthogonal Matrices](#9-orthogonal-matrices)
  - [10. Gram-Schmidt Orthogonalization](#10-gram-schmidt-orthogonalization)
- [Determinants and Eigen Theory](#determinants-and-eigen-theory)
  - [11. Determinants](#11-determinants)
  - [12. Eigenvalues and Eigenvectors](#12-eigenvalues-and-eigenvectors)
  - [13. Symmetric Matrices](#13-symmetric-matrices)
- [Matrix Factorizations](#matrix-factorizations)
  - [14. LU Decomposition](#14-lu-decomposition)
  - [15. QR Decomposition](#15-qr-decomposition)
  - [16. Singular Value Decomposition (SVD)](#16-singular-value-decomposition-svd)

---

# Concepts to learn
1. Vectors
2. Matrix Multiplication
3. Linear Systems
4. Rank
5. Orthogonality
6. Orthogonal Matrices
7. Gram-Schmidt
8. Eigenvalues and Eigenvectors
9. Symmetric Matrices
10. Singular Value Decomposition (SVD)
11. QR Decomposition
12. LU Decomposition
13. Linear Regression

# Goal
Master LU, QR, and SVD, and Linear Regression

# Linear Algebra Roadmap for LU, QR, and SVD

## 1. Vectors

Learn:

- Vector notation
- Magnitude (norm)
- Unit vectors
- Dot product
- Orthogonality

Key equations:

\[
\|\mathbf{x}\|=\sqrt{x_1^2+x_2^2+\cdots+x_n^2}
\]

\[
\mathbf{x}^T\mathbf{y}
\]


Why important:

- QR is built on orthogonal vectors.
- SVD uses orthogonal vector bases.

---

## 2. Matrix Operations

Learn:

- Matrix addition
- Matrix multiplication
- Matrix transpose
- Identity matrix
- Matrix inverse

Key concepts:

\[
AB \neq BA
\]

\[
A^{-1}A=I
\]

Why important:

- LU, QR, and SVD all factor matrices into products of matrices.

---

## 3. Linear Systems

Learn:

\[
Ax=b
\]

Understand:

- Unique solutions
- Infinite solutions
- No solutions

Why important:

- LU decomposition is primarily used to solve systems efficiently.

---

# Geometry of Linear Algebra

## 4. Linear Transformations

Learn:

\[
y=Ax
\]

Understand how matrices can:

- Rotate
- Stretch
- Compress
- Reflect
- Shear

Why important:

- SVD interprets a matrix as rotations and stretches.

---

## 5. Basis and Coordinate Systems

Learn:

- Basis vectors
- Change of basis
- Standard basis

Example:

\[
\mathbf{x}=c_1\mathbf{v}_1+c_2\mathbf{v}_2
\]

Why important:

- QR creates an orthogonal basis.
- SVD finds optimal bases.

---

## 6. Rank

Learn:

- rank of a matrix: rank(A)

Meaning:

- Number of independent directions in a matrix.

Why important:

- SVD reveals rank directly.
- Many SAR data matrices are effectively low rank.

---

## 7. Column Space and Null Space

Learn:

- Column space
- Row space
- Null space

Why important:

- Essential for understanding SVD.
- Fundamental to inverse problems and SAR imaging.

---

# Orthogonality

## 8. Orthogonal Vectors

Definition:

\[
x^Ty=0
\]

Why important:

- Foundation of QR decomposition.

---

## 9. Orthogonal Matrices

Definition:

\[
Q^TQ=I
\]

Property:

\[
Q^{-1}=Q^T
\]

Why important:

- The Q matrix in QR is orthogonal.

---

## 10. Gram-Schmidt Orthogonalization

Transforms:

\[
\{v_1,v_2,\ldots,v_n\}
\]

into

\[
\{q_1,q_2,\ldots,q_n\}
\]

where the vectors are orthogonal.

Why important:

- Classical derivation of QR decomposition.

---

# Determinants and Eigen Theory

## 11. Determinants

Learn:

\[
\det(A)
\]

Meaning:

- Volume scaling factor
- Indicates whether a matrix is invertible

Why important:

- Leads directly into eigenvalue theory.

---

## 12. Eigenvalues and Eigenvectors

Definition:

\[
A\mathbf{v}=\lambda\mathbf{v}
\]

Meaning:

- Directions preserved by the transformation.

Why important:

- Most important prerequisite for SVD.

---

## 13. Symmetric Matrices

Definition:

\[
A=A^T
\]

Why important:

Matrices such as

\[
A^TA
\]

appear directly in SVD.

Properties:

- Real eigenvalues
- Orthogonal eigenvectors

---

# Matrix Factorizations

## 14. LU Decomposition

Factorization:

\[
A=LU
\]

Where:

- L = Lower triangular matrix
- U = Upper triangular matrix

Learn:

- Gaussian elimination
- Pivoting
- Forward substitution
- Back substitution

Purpose:

- Efficiently solve linear systems.

---

## 15. QR Decomposition

Factorization:

\[
A=QR
\]

Where:

- Q = Orthogonal matrix
- R = Upper triangular matrix

Learn:

- Gram-Schmidt
- Householder reflections

Purpose:

- Least-squares solutions
- Numerical stability
- Signal processing applications

---

## 16. Singular Value Decomposition (SVD)

Factorization:

\[
A=U\Sigma V^T
\]

Where:

- U = Left singular vectors
- \(\Sigma\) = Singular values
- V = Right singular vectors

Purpose:

- Dimensionality reduction
- Noise reduction
- Pseudoinverse computation

Geometric interpretation:

1. Rotate
2. Stretch
3. Rotate again