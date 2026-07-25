function c = hypergeomcdf(N, K, n, k)
%HYPERGEOM_CDF 计算超几何分布的累积分布函数 P(X <= k)

    validate_hypergeom_params(N, K, n);

    lower = max(0, n + K - N);
    upper = min(k, n, K);
    c = 0;
    for i = lower:upper
        c = c + hypergeom_pmf(N, K, n, i);
    end
end
