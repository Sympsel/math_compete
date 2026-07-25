function p = binompmf(n, k, prob)
%BINOM_PMF 计算二项分布的概率质量函数 P(X = k)
%   n     - 实验次数（正整数）
%   k     - 成功次数（可为向量）
%   prob  - 成功概率（0 <= prob <= 1）

    validate_inputs(n, prob);
    p = nchoosek(n, k) .* (prob.^k) .* ((1 - prob).^(n - k));
end
