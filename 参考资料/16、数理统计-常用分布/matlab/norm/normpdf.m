function y = normpdf(x, mu, sigma)
%NORM_PDF 正态分布概率密度函数 f(x)
%
%   y = norm_pdf(x, mu, sigma)
%
%   输入：
%       x     - 任意实数（或向量）
%       mu    - 均值
%       sigma - 标准差（> 0）
%
%   输出：
%       y     - 概率密度值

    validate_norm(sigma);

    y = (1 / (sigma * sqrt(2 * pi))) .* exp(-((x - mu).^2) / (2 * sigma^2));
end
