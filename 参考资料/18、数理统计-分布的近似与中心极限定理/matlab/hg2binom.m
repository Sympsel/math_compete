function hg2binom(N, M, n)
    % h2binom - 计算对应的二项分布
    %
    % 输入参数：
    %   N - 样本总数
    %   M - 某一类别的样本数目
    %   n - 抽取个数
    %

    % p = M / N
    hypergeom(N, M, n)
    p = M / N;
    binom(n, p)
end