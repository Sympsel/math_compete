function p = normcdf(x, mu, sigma)
%NORM_CDF 正态分布累积分布函数 P(X <= x)

    validate_norm(sigma);

    z = (x - mu) / (sigma * sqrt(2));
    p = 0.5 * (1 + erf(z));
end
