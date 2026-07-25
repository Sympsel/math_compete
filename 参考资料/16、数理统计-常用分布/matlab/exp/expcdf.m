function p = expcdf(x, lambda)
%EXP_CDF 指数分布的累积分布函数 P(X <= x)

    validate_exp_param(lambda);

    p = zeros(size(x));
    mask = x >= 0;
    p(mask) = 1 - exp(-lambda .* x(mask));
end
