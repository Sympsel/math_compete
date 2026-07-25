function y = gammapdf(x, k, lambda)
%GAMMA_PDF 伽马分布的概率密度函数 f(x)
%
%   y = gamma_pdf(x, k, lambda)
%
%   输入：
%       x      - 输入变量（x > 0）
%       k      - 形状参数 k > 0
%       lambda - 速率参数 λ > 0
%
%   输出：
%       y      - 密度函数值

    validate_gamma_param(k, lambda);

    y = zeros(size(x));
    mask = x > 0;
    x = x(mask);

    y(mask) = (lambda^k) .* (x.^(k - 1)) .* exp(-lambda .* x) ./ gamma(k);
end
