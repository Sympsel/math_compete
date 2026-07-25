function p = poissonpmf(lambda, k)
%POISSON_PMF 计算泊松分布的概率质量函数 P(X = k)
%
%   p = poisson_pmf(lambda, k)
%
%   输入：
%       lambda - 平均事件数 λ (λ > 0)
%       k      - 非负整数（或向量）
%
%   输出：
%       p      - 概率值 P(X = k)

    validate_lambda(lambda);
    if any(k < 0)
        error('k 必须为非负整数');
    end

    p = (lambda .^ k) .* exp(-lambda) ./ factorial(k);
end
