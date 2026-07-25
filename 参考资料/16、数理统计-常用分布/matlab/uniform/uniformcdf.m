function p = uniformcdf(x, a, b)
%UNIFORM_CDF 均匀分布的累积分布函数 P(X <= x)

    validate_uniform(a, b);

    p = zeros(size(x));
    p(x < a) = 0;
    p(x >= b) = 1;
    mask = (x >= a) & (x < b);
    p(mask) = (x(mask) - a) / (b - a);
end
