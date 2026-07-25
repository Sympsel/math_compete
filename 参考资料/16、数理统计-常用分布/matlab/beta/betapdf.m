function y = betapdf(x, alpha, beta)
%BETA_PDF 计算贝塔分布的概率密度函数 f(x)
%
%   y = beta_pdf(x, alpha, beta)
%
%   输入：
%       x     - 定义域 (0,1) 上的值或向量
%       alpha - 形状参数 α > 0
%       beta  - 形状参数 β > 0
%
%   输出：
%       y     - 密度值

    validate_beta_param(alpha, beta);

    y = zeros(size(x));
    mask = (x > 0) & (x < 1);

    B = beta_func(alpha, beta);
    y(mask) = (x(mask).^(alpha - 1)) .* ((1 - x(mask)).^(beta - 1)) ./ B;
end
