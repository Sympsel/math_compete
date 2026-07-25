%% 清屏
clear all;                      %清除所有变量
close all;                      %清图
clc;                            %清屏

%% 模拟退火参数
D=2;                           % 变量维度（二维优化问题） 
Xs=1;                          % 取值范围上限                                
Xx=-1;                         % 取值范围下限

L = 200;                        % 马尔可夫链长度（每个温度下的迭代次数）
K = 0.998;                      % 温度衰减系数（0.98~0.999之间）
S = 0.01;                       % 初始扰动步长（新解生成范围控制）
T=100;                          % 初始温度（控制初始接受劣解的概率）
YZ = 1e-8;                      % 收敛判据（最优解变化阈值）
P = 0;                          % 计数：Metropolis过程中总接受点

%% ===== 初始化部分 =====
PreX = rand(D,1)*(Xs-Xx)+Xx;  % 生成初始解（D维列向量，各分量在[Xx,Xs]均匀分布）
PreBestX = PreX;              % 初始化历史最优解（用于收敛判断）

PreX =  rand(D,1)*(Xs-Xx)+Xx; % 重新生成当前解
BestX = PreX;                 % 初始化全局最优解

%% 计算初始最优解变化量
deta=abs( func1( BestX)-func1(PreBestX));

% 每迭代一次退火一次(降温), 直到满足迭代条件为止
while (T>0.001) && (deta > YZ)% 当更新变化较小 或 温度快下降至0时，结束算法
    % 温度更新（指数退火）
    T=K*T; 

    % 当前温度下的马尔可夫链迭代
    for i=1:L  
        % -- 新解生成 --
        % 在当前解附近添加随机扰动（均匀分布）
        NextX = PreX + S* (rand(D,1) *(Xs-Xx)+Xx);

        % -- 边界检查 --
        for ii=1:D
            % 若新解超出边界，则在原解附近重新生成该维度值
            if NextX(ii)>Xs | NextX(ii)<Xx
                NextX(ii)=PreX(ii) + S* (rand *(Xs-Xx)+Xx);
            end
        end            
        
        % -- 更新全局最优解 --（目前求解函数func1的最大值） 
        if (func1(BestX) < func1(NextX))
            PreBestX = BestX;  % 保存旧最优解用于收敛判断
            BestX=NextX;       % 更新全局最优解
        end


        % -- Metropolis接受准则 --
        % 计算目标函数差值（适应度改进量）
        if( func1(PreX) - func1(NextX) < 0 ) 
            PreX=NextX;    % 新解更优时必然接受
            P=P+1;         % P计数：总接受点

        else               % 新解较差时概率接受
            changer = (func1(NextX)-func1(PreX))/ T ;
            p1=exp(changer);   % 计算接受概率
            if p1 > rand       % 随机判定是否接受
                PreX=NextX;
                P=P+1;         
            end
        end
        % 记录当前最优解的目标函数值
        trace(P+1)=func1( BestX);    
    end

    % 计算最优解变化量用于收敛判断
    deta=abs( func1( BestX)-func1 (PreBestX)); 
end


%% 结果输出
disp('最大值在点:');
BestX         % 显示最优解向量
disp( '最大值为:');
func1(BestX)  % 显示最优值

%% 绘制收敛曲线
figure
plot(trace(2:end))  % 忽略初始零值
xlabel('迭代次数')
ylabel('目标函数值')
title('适应度进化曲线')