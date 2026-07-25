function p = geompmf(prob, k)
%GEOM_PMF 几何分布的概率质量函数 P(X = k)
%
%   p = geom_pmf(prob, k)
%
%   输入：
%       prob - 每次试验成功概率（0 < prob <= 1）
%       k    - 第 k 次试验成功（k ∈ {1, 2, 3, ...}）
%
%   输出：
%       p    - 成功发生在第 k 次的概率 P(X = k)

    validate_geom(prob);

    if k < 1
        p = 0;
    else
        p = (1 - prob)^(k - 1) * prob;
    end
end
