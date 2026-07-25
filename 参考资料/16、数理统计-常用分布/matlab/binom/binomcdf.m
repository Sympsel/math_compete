function c = binomcdf(n, k, prob)
%BINOM_CDF 计算二项分布的累积分布函数 P(X <= k)
%   累加 PMF 值

    validate_inputs(n, prob);

    if k < 0
        c = 0;
    elseif k >= n
        c = 1;
    else
        x = 0:floor(k);
        c = sum(binom_pmf(n, x, prob));
    end
end
