// #include <ros/ros.h>
#include <pcl/point_cloud.h>
#include <pcl_conversions/pcl_conversions.h>
#include <sensor_msgs/PointCloud2.h>
#include <pcl/io/pcd_io.h>



main (int argc, char **argv)
{
    // ros::init (argc, argv, "pcl_write_test");

    // ros::NodeHandle nh;
    pcl::PointCloud<pcl::PointXYZ>cloud_a,cloud_b,cloud_c;
    pcl::PointCloud<pcl::Normal>n_cloud_b;
    pcl::PointCloud<pcl::PointNormal>p_n_cloud_c;
    cloud_a.width=3;
    cloud_a.height=cloud_b.height=n_cloud_b.height=1;
    cloud_a.points.resize(cloud_a.width*cloud_a.height);
    if(argc!=2)
    {
        std::cerr<<"please specify command line arg '-f' or '-p'"<<std::endl;
        exit(0);
    }
    if(strcmp(argv[1],"-p")==0)
    {
        cloud_b.width=2;
        cloud_b.points.resize(cloud_b.width*cloud_b.height);
    }else
    {
        n_cloud_b.width=3;
        n_cloud_b.points.resize(n_cloud_b.width*n_cloud_b.height);
    }
    for(size_t i=0;i<cloud_a.points.size();++i)
    {
        cloud_a.points[i].x=1024*rand()/(RAND_MAX+1.0f);
        cloud_a.points[i].y=1024*rand()/(RAND_MAX+1.0f);
        cloud_a.points[i].z=1024*rand()/(RAND_MAX+1.0f);
    }
    if(strcmp(argv[1],"-p")==0)
    {
        for(size_t i=0;i<cloud_b.points.size();++i)
        {
            cloud_b.points[i].x=1024*rand()/(RAND_MAX+1.0f);
            cloud_b.points[i].y=1024*rand()/(RAND_MAX+1.0f);
            cloud_b.points[i].z=1024*rand()/(RAND_MAX+1.0f);
        }
    }else
    {
        for(size_t i=0;i<n_cloud_b.points.size();++i)
        {
            n_cloud_b.points[i].normal[0]=1024*rand()/(RAND_MAX+1.0f);
            n_cloud_b.points[i].normal[1]=1024*rand()/(RAND_MAX+1.0f);
            n_cloud_b.points[i].normal[2]=1024*rand()/(RAND_MAX+1.0f);
        }
    }
    std::cerr<<"Cloud A:"<<std::endl;
    for(size_t i=0;i<cloud_a.points.size();++i)
    {
        std::cerr<<"  "<<cloud_a.points[i].x<<"  "<<cloud_a.points[i].y<<"  "<<cloud_a.points[i].z<<std::endl;
    }
    std::cerr<<"Cloud B:"<<std::endl;
    if(strcmp(argv[1],"-p")==0)
    {
        for(size_t i=0;i<cloud_b.points.size();++i)
        {
            std::cerr<<"  "<<cloud_b.points[i].x<<"  "<<cloud_b.points[i].y<<"  "<<cloud_b.points[i].z<<std::endl;
        }
    }else
    {
        for(size_t i=0;i<n_cloud_b.points.size();++i)
        {
            std::cerr<<" n_cloud_b "<<n_cloud_b.points[i].normal[0]<<"  "<<n_cloud_b.points[i].normal[1]<<"  "<<n_cloud_b.points[i].normal[2]<<std::endl;
        }
    }
    if(strcmp(argv[1],"-p")==0)
    {
        cloud_c=cloud_a;
        cloud_c+=cloud_b;
        std::cerr<<"Cloud C: "<<std::endl;
        for(size_t i=0;i<cloud_c.points.size();++i)
        {
            std::cerr<<"    "<<cloud_c.points[i].x<<" "<<cloud_c.points[i].y<<" "<<cloud_c.points[i].z<<" "<<std::endl;
        }
        
    }else
    {
        pcl::concatenateFields(cloud_a,n_cloud_b,p_n_cloud_c);
        std::cerr<<"p_n_cloud_c: "<<std::endl;
        for(size_t i=0;i<p_n_cloud_c.points.size();++i)
        std::cerr<<"    "<<p_n_cloud_c.points[i].x<<" "<<p_n_cloud_c.points[i].y<<" "<<p_n_cloud_c.points[i].z<<" "<<p_n_cloud_c.points[i].normal[0]<<" "<<p_n_cloud_c.points[i].normal[1]<<" "<<p_n_cloud_c.points[i].normal[2]<<std::endl;
    }
    
    // pcl::PointCloud<pcl::PointXYZ> cloud;
    // cloud.width=5;
    // cloud.height=1;
    // cloud.is_dense=false;
    // cloud.points.resize(cloud.width*cloud.height);
    // for(size_t i=0;i<cloud.points.size();++i)
    // {
    //     cloud.points[i].x=1024*rand()/(RAND_MAX+1.0f);
    //     cloud.points[i].y=1024*rand()/(RAND_MAX+1.0f);
    //     cloud.points[i].z=1024*rand()/(RAND_MAX+1.0f);
    // }
    // pcl::io::savePCDFileASCII("test_pcd_write.pcd",cloud);
    // std::cerr<<"saved"<<cloud.points.size()<<"data points to test_pcd.pcd"<<std::endl;
    // for(size_t i=0;i<cloud.points.size();++i)
    // {
    //     std::cerr<<"  "<<cloud.points[i].x<<"  "<<cloud.points[i].y<<"  "<<cloud.points[i].z<<std::endl;
    // }

    // ros::spin();

    return 0;
}

