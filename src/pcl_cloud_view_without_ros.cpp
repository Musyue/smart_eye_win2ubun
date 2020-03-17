// #include <ros/ros.h>
#include <pcl/point_cloud.h>
#include <pcl/visualization/cloud_viewer.h>
#include <sensor_msgs/PointCloud2.h>
#include <pcl/io/pcd_io.h>
#include <pcl/io/io.h>
#include <vector>
#include <ctime>
int user_data;
void viewerOneOff(pcl::visualization::PCLVisualizer& viewer)
{
    viewer.setBackgroundColor(0.0,0.5,1.0);
    pcl::PointXYZ o;
    o.x=1.0;
    o.y=0;
    o.z=0;
    viewer.addSphere(o,0.25,"sphere",0);
    std::cout<<"I only run one time"<<std::endl;
}
void viewerPsycho(pcl::visualization::PCLVisualizer& viewer)
{
    static unsigned count=0;
    std::stringstream ss;
    ss<<"Once per viewer loop:"<<count++;
    viewer.removeShape("text",0);
    viewer.addText(ss.str(),200,300,"text",0);
    user_data++;
}
main (int argc, char **argv)
{
    // ros::init (argc, argv, "pcl_write_test");

    // ros::NodeHandle nh;
    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>);
    pcl::io::loadPCDFile("maize.pcd",*cloud);
    pcl::visualization::CloudViewer viewer("Cloud Viewer");
    viewer.showCloud(cloud);
    viewer.runOnVisualizationThreadOnce(viewerOneOff);
    viewer.runOnVisualizationThread(viewerPsycho);
    while(!viewer.wasStopped())
    {
        user_data++;
    }
    // ros::spin();

    return 0;
}

