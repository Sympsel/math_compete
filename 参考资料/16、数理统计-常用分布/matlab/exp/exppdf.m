function y = exppdf(x, lambda)
%EXP_PDF 指数分布的概率密度函数 f(x)
%
%   y = exp_pdf(x, lambda)
%
%   输入：
%       x      - 输入变量（可为标量或向量）
%       lambda - 速率参数 λ（> 0）
%
%   输出：
%       y      - 对应概率密度值

    validate_exp_param(lambda);

    y = zeros(size(x));
    mask = x >= 0;
    y(mask) = lambda .* exp(-lambda .* x(mask));
end
