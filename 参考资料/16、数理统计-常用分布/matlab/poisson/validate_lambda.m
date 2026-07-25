function validate_lambda(lambda)
%VALIDATE_LAMBDA 检查 λ 的合法性

    if ~isscalar(lambda) || lambda <= 0
        error('λ 必须为正数标量');
    end
end
