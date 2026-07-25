function p = hypergeompmf(N, K, n, k)
%HYPERGEOM_PMF 计算超几何分布的概率质量函数 P(X = k)
%
%   p = hypergeom_pmf(N, K, n, k)
%
%   输入：
%       N - 总体容量
%       K - 成功元素总数
%       n - 抽样次数
%       k - 抽中成功元素数量
%
%   输出：
%       p - 概率值 P(X = k)

    validate_hypergeom_params(N, K, n);

    if k < 0 || k > n || k > K || n - k > N - K
        p = 0;
    else
        p = nchoosek(K, k) * nchoosek(N - K, n - k) / nchoosek(N, n);
    end
end
