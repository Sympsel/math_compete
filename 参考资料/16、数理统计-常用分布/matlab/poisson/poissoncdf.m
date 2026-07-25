function c = poissoncdf(lambda, k)
%POISSON_CDF 计算泊松分布的累积分布函数 P(X <= k)
%
%   c = poisson_cdf(lambda, k)

    validate_lambda(lambda);

    if k < 0
        c = 0;
    else
        x = 0:floor(k);
        c = sum(poisson_pmf(lambda, x));
    end
end
