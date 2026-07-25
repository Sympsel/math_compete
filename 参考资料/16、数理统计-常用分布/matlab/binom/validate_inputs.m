function validate_inputs(n, prob)
%VALIDATE_INPUTS 检查输入合法性

    if ~isscalar(n) || n <= 0 || floor(n) ~= n
        error('实验次数 n 必须为正整数。');
    end
    if ~isscalar(prob) || prob < 0 || prob > 1
        error('成功概率 prob 必须在 [0, 1] 范围内。');
    end
end
