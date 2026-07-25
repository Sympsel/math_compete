% 林德伯格-莱维CLT
fprintf("P(S_100 ≤ 220) ≈%.4f\n", lind_clt(220, 2, 4, 100))

% 德莫弗—拉普拉斯 CLT：Binom(50, 0.3)
fprintf("P(X ≤ 20) ≈%.4f\n", laplace_clt(20, 50, 0.3))