function y = uniformpdf(x, a, b)
%UNIFORM_PDF 均匀分布的概率密度函数 f(x)
%
%   y = uniform_pdf(x, a, b)
%
%   输入：
%       x - 输入变量
%       a - 区间左端点
%       b - 区间右端点（必须 a < b）
%
%   输出：
%       y - 密度值 f(x)

    validate_uniform(a, b);

    y = zeros(size(x));
    mask = (x >= a) & (x <= b);
    y(mask) = 1 / (b - a);
end
